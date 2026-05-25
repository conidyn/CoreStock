import { Card } from "@/components/ui/Card";

const recentMovements = [
    {
        id: 1,
        product: "Dell Latitude 5450",
        type: "Purchase",
        quantity: 12,
        location: "Liège Main Warehouse",
    },
    {
        id: 2,
        product: "Logitech MX Keys",
        type: "Transfer",
        quantity: 5,
        location: "Brussels Secondary Warehouse",
    },
    {
        id: 3,
        product: "Zebra Label Printer",
        type: "Sale",
        quantity: 2,
        location: "Demo Customer",
    },
];

export function RecentMovements() {
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

            <div className="space-y-4">
                {recentMovements.map((movement) => (
                    <div
                        key={movement.id}
                        className="flex items-center justify-between border-b border-slate-800 pb-4 last:border-0 last:pb-0"
                    >
                        <div>
                            <p className="font-medium text-slate-100">{movement.product}</p>
                            <p className="mt-1 text-sm text-slate-500">
                                {movement.type} · {movement.location}
                            </p>
                        </div>

                        <p className="text-sm font-semibold text-slate-300">
                            {movement.quantity} units
                        </p>
                    </div>
                ))}
            </div>
        </Card>
    );
}