import type { StockLocation } from "@/lib/locations-api";

import { Card } from "@/components/ui/Card";

type LocationTableProps = {
    locations: StockLocation[];
};

export function LocationTable({ locations }: LocationTableProps) {
    return (
        <Card>
            <div className="mb-6">
                <h2 className="text-lg font-semibold text-slate-100">Locations</h2>
                <p className="mt-1 text-sm text-slate-500">
                    Warehouses, suppliers and customer destinations used in stock flows.
                </p>
            </div>

            <div className="overflow-hidden rounded-xl border border-slate-800">
                <table className="w-full border-collapse text-left text-sm">
                    <thead className="bg-slate-900">
                        <tr className="border-b border-slate-800 text-slate-400">
                            <th className="px-4 py-3 font-medium">Location</th>
                            <th className="px-4 py-3 font-medium">Type</th>
                        </tr>
                    </thead>

                    <tbody>
                        {locations.map((location) => (
                            <tr
                                key={location.id}
                                className="border-b border-slate-800 last:border-0"
                            >
                                <td className="px-4 py-4 font-medium text-slate-100">
                                    {location.name}
                                </td>
                                <td className="px-4 py-4 text-slate-400">{location.type}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </Card>
    );
}