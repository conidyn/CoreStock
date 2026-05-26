import { Card } from "@/components/ui/Card";
import { StockItem } from "@/lib/stock-items-api";

type StockByLocationProps = {
    stockItems: StockItem[];
};

export function StockByLocation({
    stockItems,
}: StockByLocationProps) {
    const groupedLocations = Object.values(
        stockItems.reduce(
            (accumulator, stockItem) => {
                const locationId = stockItem.location.id;

                if (!accumulator[locationId]) {
                    accumulator[locationId] = {
                        locationName: stockItem.location.name,
                        locationType: stockItem.location.type,
                        items: [],
                    };
                }

                accumulator[locationId].items.push(stockItem);

                return accumulator;
            },
            {} as Record<
                number,
                {
                    locationName: string;
                    locationType: string;
                    items: StockItem[];
                }
            >
        )
    );

    return (
        <Card>
            <div className="mb-6">
                <h2 className="text-lg font-semibold text-slate-100">
                    Stock by location
                </h2>

                <p className="mt-1 text-sm text-slate-500">
                    Current inventory distribution across warehouses.
                </p>
            </div>

            <div className="space-y-6">
                {groupedLocations.map((location) => (
                    <div
                        key={location.locationName}
                        className="rounded-xl border border-slate-800"
                    >
                        <div className="border-b border-slate-800 bg-slate-900 px-4 py-3">
                            <div className="flex items-center justify-between">
                                <h3 className="font-medium text-slate-100">
                                    {location.locationName}
                                </h3>

                                <span className="text-xs uppercase tracking-wide text-slate-500">
                                    {location.locationType}
                                </span>
                            </div>
                        </div>

                        <div className="divide-y divide-slate-800">
                            {location.items.map((item) => (
                                <div
                                    key={item.id}
                                    className="flex items-center justify-between px-4 py-3"
                                >
                                    <div>
                                        <p className="font-medium text-slate-100">
                                            {item.product.name}
                                        </p>

                                        <p className="text-sm text-slate-500">
                                            {item.product.sku}
                                        </p>
                                    </div>

                                    <p className="text-sm font-medium text-slate-300">
                                        {item.quantity} units
                                    </p>
                                </div>
                            ))}
                        </div>
                    </div>
                ))}
            </div>
        </Card>
    );
}