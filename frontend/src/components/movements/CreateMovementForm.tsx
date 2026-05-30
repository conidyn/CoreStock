"use client";

import { useRouter } from "next/navigation";
import { FormEvent, useMemo, useState } from "react";

import { Card } from "@/components/ui/Card";
import {
    createStockMovement,
    type CreateStockMovementPayload,
} from "@/lib/movements-api";
import { Product } from "@/lib/products-api";
import { StockLocation } from "@/lib/locations-api";
import { StockItem } from "@/lib/stock-items-api";

type CreateMovementFormProps = {
    products: Product[];
    locations: StockLocation[];
    stockItems: StockItem[];
};

type MovementType = CreateStockMovementPayload["movement_type"];

const movementRules: Record<
    MovementType,
    {
        sourceType: StockLocation["type"];
        destinationType: StockLocation["type"];
        helperText: string;
    }
> = {
    purchase: {
        sourceType: "supplier",
        destinationType: "internal",
        helperText: "Purchase: supplier → warehouse",
    },
    sale: {
        sourceType: "internal",
        destinationType: "customer",
        helperText: "Sale: warehouse → customer",
    },
    transfer: {
        sourceType: "internal",
        destinationType: "internal",
        helperText: "Transfer: warehouse → warehouse",
    },
};

export function CreateMovementForm({
    products,
    locations,
    stockItems,
}: CreateMovementFormProps) {
    const router = useRouter();

    const [productId, setProductId] = useState("");
    const [movementType, setMovementType] = useState<MovementType>("purchase");
    const [fromLocationId, setFromLocationId] = useState("");
    const [toLocationId, setToLocationId] = useState("");
    const [quantity, setQuantity] = useState("");
    const [reason, setReason] = useState("");

    const [isSubmitting, setIsSubmitting] = useState(false);
    const [errorMessage, setErrorMessage] = useState<string | null>(null);
    const [successMessage, setSuccessMessage] = useState<string | null>(null);

    const currentRule = movementRules[movementType];

    const sourceLocations = useMemo(
        () =>
            locations.filter((location) => location.type === currentRule.sourceType),
        [locations, currentRule.sourceType]
    );

    const destinationLocations = useMemo(
        () =>
            locations.filter((location) => {
                const matchesDestinationType =
                    location.type === currentRule.destinationType;

                if (movementType !== "transfer") {
                    return matchesDestinationType;
                }

                return (
                    matchesDestinationType &&
                    location.id !== Number(fromLocationId)
                );
            }),
        [locations, currentRule.destinationType, movementType, fromLocationId]
    );

    const availableProducts = useMemo(() => {
        if (movementType === "purchase") {
            return products;
        }

        if (!fromLocationId) {
            return [];
        }

        const availableProductIds = new Set(
            stockItems
                .filter(
                    (stockItem) =>
                        stockItem.location.id === Number(fromLocationId) &&
                        stockItem.quantity > 0
                )
                .map((stockItem) => stockItem.product.id)
        );

        return products.filter((product) => availableProductIds.has(product.id));
    }, [products, stockItems, movementType, fromLocationId]);

    const selectedStockItem = useMemo(() => {
        if (movementType === "purchase" || !fromLocationId || !productId) {
            return null;
        }

        return (
            stockItems.find(
                (stockItem) =>
                    stockItem.location.id === Number(fromLocationId) &&
                    stockItem.product.id === Number(productId)
            ) ?? null
        );
    }, [stockItems, movementType, fromLocationId, productId]);

    const availableQuantity = selectedStockItem?.quantity ?? null;

    function handleMovementTypeChange(value: MovementType) {
        setMovementType(value);
        setFromLocationId("");
        setToLocationId("");
        setProductId("");
        setQuantity("");
        setErrorMessage(null);
        setSuccessMessage(null);
    }

    function buildSuccessMessage() {
        const selectedProduct = products.find(
            (product) => product.id === Number(productId)
        );

        const sourceLocation = locations.find(
            (location) => location.id === Number(fromLocationId)
        );

        const destinationLocation = locations.find(
            (location) => location.id === Number(toLocationId)
        );

        if (!selectedProduct || !sourceLocation || !destinationLocation) {
            return "Stock movement created successfully.";
        }

        if (movementType === "purchase") {
            return `Purchased ${quantity} ${selectedProduct.name} into ${destinationLocation.name}.`;
        }

        if (movementType === "transfer") {
            return `Transferred ${quantity} ${selectedProduct.name} from ${sourceLocation.name} to ${destinationLocation.name}.`;
        }

        return `Sold ${quantity} ${selectedProduct.name} to ${destinationLocation.name}.`;
    }

    async function handleSubmit(event: FormEvent<HTMLFormElement>) {
        event.preventDefault();

        if (!productId || !fromLocationId || !toLocationId || !quantity || !reason) {
            setErrorMessage("Please complete all fields before creating a movement.");
            return;
        }
        if (
            movementType !== "purchase" &&
            availableQuantity !== null &&
            Number(quantity) > availableQuantity
        ) {
            setErrorMessage(
                `Quantity cannot exceed available stock (${availableQuantity}).`
            );

            return;
        }

        setIsSubmitting(true);
        setErrorMessage(null);
        setSuccessMessage(null);

        try {
            await createStockMovement({
                product_id: Number(productId),
                from_location_id: Number(fromLocationId),
                to_location_id: Number(toLocationId),
                quantity: Number(quantity),
                movement_type: movementType,
                reason,
            });
            const successMessage = buildSuccessMessage();
            setProductId("");
            setMovementType("purchase");
            setFromLocationId("");
            setToLocationId("");
            setQuantity("");
            setReason("");
            setSuccessMessage(successMessage);

            router.refresh();
        } catch (error) {
            if (error instanceof Error) {
                setErrorMessage(error.message);
            } else {
                setErrorMessage("Unexpected error while creating movement.");
            }
        } finally {
            setIsSubmitting(false);
        }
    }

    return (
        <Card>
            <div className="mb-6">
                <h2 className="text-lg font-semibold text-slate-100">
                    Create stock movement
                </h2>

                <p className="mt-1 text-sm text-slate-500">
                    Register purchases, transfers and customer shipments.
                </p>

                <p className="mt-3 rounded-xl border border-slate-800 bg-slate-950 px-4 py-3 text-sm text-slate-400">
                    {currentRule.helperText}
                </p>
            </div>

            <form onSubmit={handleSubmit} className="grid gap-4 md:grid-cols-2">
                <div>
                    <label className="mb-2 block text-sm text-slate-400">
                        Movement type
                    </label>

                    <select
                        value={movementType}
                        onChange={(event) =>
                            handleMovementTypeChange(event.target.value as MovementType)
                        }
                        className="w-full rounded-xl border border-slate-800 bg-slate-950 px-4 py-3 text-sm text-slate-100 outline-none"
                    >
                        <option value="purchase">Purchase</option>
                        <option value="transfer">Transfer</option>
                        <option value="sale">Sale</option>
                    </select>
                </div>

                <div>
                    <label className="mb-2 block text-sm text-slate-400">Reason</label>

                    <input
                        type="text"
                        value={reason}
                        onChange={(event) => setReason(event.target.value)}
                        placeholder="Movement reason"
                        required
                        minLength={3}
                        maxLength={50}
                        className="w-full rounded-xl border border-slate-800 bg-slate-950 px-4 py-3 text-sm text-slate-100 outline-none"
                    />
                </div>

                <div>
                    <label className="mb-2 block text-sm text-slate-400">
                        Source location
                    </label>

                    <select
                        value={fromLocationId}
                        onChange={(event) => {
                            setFromLocationId(event.target.value);
                            setToLocationId("");
                            setProductId("");
                        }}
                        required
                        className="w-full rounded-xl border border-slate-800 bg-slate-950 px-4 py-3 text-sm text-slate-100 outline-none"
                    >
                        <option value="">Select source location</option>

                        {sourceLocations.map((location) => (
                            <option key={location.id} value={location.id}>
                                {location.name}
                            </option>
                        ))}
                    </select>
                </div>

                <div>
                    <label className="mb-2 block text-sm text-slate-400">
                        Destination location
                    </label>

                    <select
                        value={toLocationId}
                        onChange={(event) => setToLocationId(event.target.value)}
                        required
                        className="w-full rounded-xl border border-slate-800 bg-slate-950 px-4 py-3 text-sm text-slate-100 outline-none"
                    >
                        <option value="">Select destination location</option>

                        {destinationLocations.map((location) => (
                            <option key={location.id} value={location.id}>
                                {location.name}
                            </option>
                        ))}
                    </select>
                </div>

                <div>
                    <label className="mb-2 block text-sm text-slate-400">Product</label>

                    <select
                        value={productId}
                        onChange={(event) => {
                            setProductId(event.target.value);
                            setQuantity("");
                        }}
                        disabled={
                            movementType !== "purchase" &&
                            !fromLocationId
                        }
                        required
                        className="w-full rounded-xl border border-slate-800 bg-slate-950 px-4 py-3 text-sm text-slate-100 outline-none disabled:cursor-not-allowed disabled:opacity-50"
                    >
                        <option value="">
                            {movementType === "purchase" || fromLocationId
                                ? "Select a product"
                                : "Select a source location first"}
                        </option>

                        {availableProducts.map((product) => (
                            <option key={product.id} value={product.id}>
                                {product.name}
                            </option>
                        ))}
                    </select>
                    {movementType !== "purchase" &&
                        fromLocationId &&
                        availableProducts.length === 0 && (
                            <p className="mt-2 text-xs text-amber-400">
                                No products available in selected warehouse.
                            </p>
                        )}

                </div>

                <div>
                    <label className="mb-2 block text-sm text-slate-400">Quantity</label>

                    <input
                        type="number"
                        min="1"
                        max={
                            movementType === "purchase"
                                ? undefined
                                : availableQuantity ?? undefined
                        }
                        value={quantity}
                        onChange={(event) => setQuantity(event.target.value)}
                        required
                        className="w-full rounded-xl border border-slate-800 bg-slate-950 px-4 py-3 text-sm text-slate-100 outline-none"
                    />
                    {movementType !== "purchase" && availableQuantity !== null && (
                        <p className="mt-2 text-xs text-slate-500">
                            Available stock: {availableQuantity} units
                        </p>
                    )}
                </div>

                {errorMessage && (
                    <p className="md:col-span-2 text-sm text-red-400">{errorMessage}</p>
                )}

                {successMessage && (
                    <p className="md:col-span-2 text-sm text-emerald-400">
                        {successMessage}
                    </p>
                )}

                <div className="md:col-span-2">
                    <button
                        type="submit"
                        disabled={
                            isSubmitting ||
                            (
                                movementType !== "purchase" &&
                                availableProducts.length === 0
                            )
                        }
                        className="rounded-xl bg-slate-100 px-5 py-3 text-sm font-medium text-slate-950 transition hover:bg-white disabled:cursor-not-allowed disabled:opacity-60"
                    >
                        {isSubmitting ? "Creating..." : "Create movement"}
                    </button>
                </div>
            </form>
        </Card>
    );
}