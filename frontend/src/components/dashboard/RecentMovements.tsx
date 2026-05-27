import { Card } from "@/components/ui/Card";
import { StockMovement } from "@/lib/movements-api";

type RecentMovementsProps = {
    movements: StockMovement[];
};

function formatMovementDate(date: string) {
    return new Intl.DateTimeFormat("en-GB", {
        day: "2-digit",
        month: "short",
        year: "numeric",
        hour: "2-digit",
        minute: "2-digit",
    })
        .format(new Date(date))
        .replace(",", " ·") + " UTC";
}

function formatMovementType(type: StockMovement["movement_type"]) {
    return type.charAt(0).toUpperCase() + type.slice(1);
}

export function RecentMovements({ movements }: RecentMovementsProps) {
    return (
        <Card className="mt-6">
            <div className="mb-6">
                <h2 className="text-lg font-semibold text-slate-100">
                    Recent movements
                </h2>
                <p className="mt-1 text-sm text-slate-500">
                    Latest stock operations across warehouses.
                </p>
            </div>

            {movements.length === 0 ? (
                <p className="text-sm text-slate-500">
                    No recent stock movement yet.
                </p>
            ) : (
                <div className="space-y-4">
                    {movements.map((movement) => (
                        <div
                            key={movement.id}
                            className="flex items-center justify-between border-b border-slate-800 pb-4 last:border-0 last:pb-0"
                        >
                            <div>
                                <p className="font-medium text-slate-100">
                                    {movement.product.name}
                                </p>
                                <div className="mt-1 space-y-1">
                                    <p className="text-sm text-slate-500">
                                        {formatMovementType(movement.movement_type)} ·{" "}
                                        {movement.from_location.name} → {movement.to_location.name}
                                    </p>

                                    <p className="text-xs text-slate-600">
                                        {formatMovementDate(movement.created_at)}
                                    </p>
                                </div>
                            </div>

                            <p className="text-sm font-semibold text-slate-300">
                                {movement.quantity} units
                            </p>
                        </div>
                    ))}
                </div>
            )}
        </Card>
    );
}