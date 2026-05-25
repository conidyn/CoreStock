import { Card } from "@/components/ui/Card";

const products = [
    {
        id: 1,
        name: "Dell Latitude 5450",
        sku: "WH-LIEGE-APP-001",
        category: "IT Equipment",
        unit: "unit",
        minStockThreshold: 5,
    },
    {
        id: 2,
        name: "Logitech MX Keys",
        sku: "WH-LIEGE-ACC-002",
        category: "Accessories",
        unit: "unit",
        minStockThreshold: 10,
    },
    {
        id: 3,
        name: "Zebra Label Printer",
        sku: "WH-BXL-PRT-003",
        category: "Warehouse Equipment",
        unit: "unit",
        minStockThreshold: 3,
    },
];

export function ProductTable() {
    return (
        <Card>
            <div className="mb-6">
                <h2 className="text-lg font-semibold text-slate-100">
                    Products
                </h2>
                <p className="mt-1 text-sm text-slate-500">
                    Demo product catalog with SKU, category and stock threshold.
                </p>
            </div>

            <div className="overflow-hidden rounded-xl border border-slate-800">
                <table className="w-full border-collapse text-left text-sm">
                    <thead className="bg-slate-900">
                        <tr className="border-b border-slate-800 text-slate-400">
                            <th className="px-4 py-3 font-medium">Product</th>
                            <th className="px-4 py-3 font-medium">SKU</th>
                            <th className="px-4 py-3 font-medium">Category</th>
                            <th className="px-4 py-3 font-medium">Unit</th>
                            <th className="px-4 py-3 font-medium">Min. stock</th>
                        </tr>
                    </thead>

                    <tbody>
                        {products.map((product) => (
                            <tr
                                key={product.id}
                                className="border-b border-slate-800 last:border-0"
                            >
                                <td className="px-4 py-4 font-medium text-slate-100">
                                    {product.name}
                                </td>
                                <td className="px-4 py-4 text-slate-400">{product.sku}</td>
                                <td className="px-4 py-4 text-slate-400">
                                    {product.category}
                                </td>
                                <td className="px-4 py-4 text-slate-400">{product.unit}</td>
                                <td className="px-4 py-4 text-slate-400">
                                    {product.minStockThreshold}
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </Card>
    );
}