"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

type ResetStatus = "idle" | "loading" | "success" | "error";

export function DemoResetControl() {
    const router = useRouter();
    const [status, setStatus] = useState<ResetStatus>("idle");
    const [message, setMessage] = useState<string | null>(null);

    async function handleReset() {
        setStatus("loading");
        setMessage(null);

        try {
            const response = await fetch("/api/demo/reset", {
                method: "POST",
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.detail || "Failed to reset demo environment");
            }

            setStatus("success");
            setMessage(data.message || "Demo environment successfully restored");
            router.refresh();
        } catch (error) {
            setStatus("error");
            setMessage(
                error instanceof Error
                    ? error.message
                    : "Failed to reset demo environment"
            );
        }
    }

    return (
        <div className="mt-8 flex flex-col items-start gap-4">
            <p className="text-sm text-slate-500">
                Demo reset cooldown: 5 minutes
            </p>

            <button
                type="button"
                onClick={handleReset}
                disabled={status === "loading"}
                className="rounded-xl border border-blue-500/30 bg-blue-500/10 px-6 py-3 text-sm font-semibold text-blue-200 transition hover:border-blue-400 hover:bg-blue-500/20 disabled:cursor-not-allowed disabled:opacity-60"
            >
                {status === "loading"
                    ? "Resetting demo environment..."
                    : "Reset Demo Environment"}
            </button>

            {message && (
                <p
                    className={
                        status === "success"
                            ? "text-sm text-emerald-300"
                            : "text-sm text-amber-300"
                    }
                >
                    {message}
                </p>
            )}
        </div>
    );
}