import type { ReactNode } from "react";

type CardProps = {
    children: ReactNode;
    className?: string;
};

export function Card({
    children,
    className = "",
}: CardProps) {
    return (
        <div
            className={`rounded-2xl border border-slate-800 bg-slate-900/60 p-6 shadow-sm ${className}`}
        >
            {children}
        </div>
    );
}