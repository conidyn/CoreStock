export default function HomePage() {
  return (
    <main className="min-h-screen bg-slate-950 text-slate-100">
      <div className="mx-auto flex min-h-screen max-w-7xl items-center justify-center px-6">
        <div className="text-center">
          <p className="mb-3 text-sm font-medium uppercase tracking-[0.3em] text-slate-500">
            CoreStock
          </p>

          <h1 className="text-5xl font-bold tracking-tight">
            ERP / WMS Inventory Platform
          </h1>

          <p className="mt-6 max-w-2xl text-lg text-slate-400">
            Modern supply chain and inventory management dashboard inspired by
            real ERP and warehouse management workflows.
          </p>
        </div>
      </div>
    </main>
  );
}