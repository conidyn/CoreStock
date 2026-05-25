import { Card } from "@/components/ui/Card";

type KpiCardProps = {
    label: string;
    value: string | number;
    helperText: string;
};

export function KpiCard({ label, value, helperText }: KpiCardProps) {
    return (
        <Card>
            <p className="text-sm font-medium text-slate-400">{label}</p>

            <p className="mt-3 text-3xl font-bold tracking-tight text-slate-100">
                {value}
            </p>

            <p className="mt-2 text-sm text-slate-500">{helperText}</p>
        </Card>
    );
}