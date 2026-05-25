import { Card } from "@/components/ui/Card";

const movements = [
    {
        id: 1,
        product: "Dell Latitude 5450",
        type: "Purchase",
        source: "TechSupplier Europe",
        destination: "Liège Main Warehouse",
        quantity: 12,
        date: "2026-05-25",
        status: "Done",
    },
    {
        id: 2,
        product: "Logitech MX Keys",
        type: "Transfer",
        source: "Liège Main Warehouse",
        destination: "Brussels Secondary Warehouse",
        quantity: 5,
        date: "2026-05-25",
        status: "Done",
    },
    {
        id: 3,
        product: "Zebra Label Printer",
        type: "Sale",
        source: "Liège Main Warehouse",
        destination: "Demo Customer",
        quantity: 2,
        date: "2026-05-24",
        status: "Done",
    },
];

export function MovementTable() {
    return (
        <Card>
            <div className="mb-6">
                <h2 className="text-lg font-semibold text-slate-100">
                    Stock movements
                </h2>
                <p className="mt-1 text-sm text-slate-500">
                    Traceability of purchase, sale and internal transfer operations.
                </p>
            </div>

            <div className="overflow-x-auto rounded-xl border border-slate-800">
                <table className="w-full border-collapse text-left text-sm">
                    <thead className="bg-slate-900">
                        <tr className="border-b border-slate-800 text-slate-400">
                            <th className="px-4 py-3 font-medium">Product</th>
                            <th className="px-4 py-3 font-medium">Type</th>
                            <th className="px-4 py-3 font-medium">Source</th>
                            <th className="px-4 py-3 font-medium">Destination</th>
                            <th className="px-4 py-3 font-medium">Quantity</th>
                            <th className="px-4 py-3 font-medium">Date</th>
                            <th className="px-4 py-3 font-medium">Status</th>
                        </tr>
                    </thead>

                    <tbody>
                        {movements.map((movement) => (
                            <tr
                                key={movement.id}
                                className="border-b border-slate-800 last:border-0"
                            >
                                <td className="px-4 py-4 font-medium text-slate-100">
                                    {movement.product}
                                </td>
                                <td className="px-4 py-4 text-slate-400">{movement.type}</td>
                                <td className="px-4 py-4 text-slate-400">{movement.source}</td>
                                <td className="px-4 py-4 text-slate-400">
                                    {movement.destination}
                                </td>
                                <td className="px-4 py-4 text-slate-400">
                                    {movement.quantity}
                                </td>
                                <td className="px-4 py-4 text-slate-400">{movement.date}</td>
                                <td className="px-4 py-4 text-slate-400">{movement.status}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </Card>
    );
}