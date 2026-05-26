import { DashboardLayout } from "@/components/layout/DashboardLayout";
import { ProductTable } from "@/components/products/ProductTable";
import { getProducts } from "@/lib/products-api";
import { getStockItems } from "@/lib/stock-items-api";

export const dynamic = "force-dynamic";

export default async function ProductsPage() {
    const products = await getProducts();
    const stockItems = await getStockItems();

    return (
        <DashboardLayout>
            <div className="w-full max-w-7xl py-10">
                <div className="mb-10">
                    <p className="text-sm font-medium uppercase tracking-[0.3em] text-slate-500">
                        Products
                    </p>

                    <h1 className="mt-3 text-4xl font-bold tracking-tight text-slate-100">
                        Product Catalog
                    </h1>

                    <p className="mt-3 text-lg text-slate-400">
                        Track products, SKUs, categories, stock thresholds and total inventory across warehouses.
                    </p>
                </div>

                <ProductTable products={products} stockItems={stockItems} />
            </div>
        </DashboardLayout>
    );
}