import type { StockMovement } from "@/lib/movements-api";

import { Card } from "@/components/ui/Card";

type MovementTableProps = {
    movements: StockMovement[];
};

export function MovementTable({ movements }: MovementTableProps) {
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
                            <th className="px-4 py-3 font-medium">Reason</th>
                        </tr>
                    </thead>

                    <tbody>
                        {movements.map((movement) => (
                            <tr
                                key={movement.id}
                                className="border-b border-slate-800 last:border-0"
                            >
                                <td className="px-4 py-4 font-medium text-slate-100">
                                    {movement.product.name}
                                </td>
                                <td className="px-4 py-4 text-slate-400">
                                    {movement.movement_type}
                                </td>
                                <td className="px-4 py-4 text-slate-400">
                                    {movement.from_location.name}
                                </td>
                                <td className="px-4 py-4 text-slate-400">
                                    {movement.to_location.name}
                                </td>
                                <td className="px-4 py-4 text-slate-400">
                                    {movement.quantity}
                                </td>
                                <td className="px-4 py-4 text-slate-400">
                                    {new Date(movement.created_at).toLocaleDateString()}
                                </td>
                                <td className="px-4 py-4 text-slate-400">
                                    {movement.reason}
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </Card>
    );
}