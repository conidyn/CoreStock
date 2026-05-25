import { Card } from "@/components/ui/Card";

const locations = [
    {
        id: 1,
        name: "Liège Main Warehouse",
        type: "Internal",
        city: "Liège",
        country: "Belgium",
        status: "Active",
    },
    {
        id: 2,
        name: "TechSupplier Europe",
        type: "Supplier",
        city: "Luxembourg",
        country: "Luxembourg",
        status: "Active",
    },
    {
        id: 3,
        name: "Demo Customer",
        type: "Customer",
        city: "Brussels",
        country: "Belgium",
        status: "Active",
    },
];

export function LocationTable() {
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
                            <th className="px-4 py-3 font-medium">City</th>
                            <th className="px-4 py-3 font-medium">Country</th>
                            <th className="px-4 py-3 font-medium">Status</th>
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
                                <td className="px-4 py-4 text-slate-400">{location.city}</td>
                                <td className="px-4 py-4 text-slate-400">
                                    {location.country}
                                </td>
                                <td className="px-4 py-4 text-slate-400">{location.status}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </Card>
    );
}