import { NextResponse } from "next/server";
import { API_BASE_URL } from "@/config/api";

export async function POST() {
  const demoResetToken = process.env.DEMO_RESET_TOKEN;

  if (!demoResetToken) {
    return NextResponse.json(
      { detail: "Demo reset token is not configured" },
      { status: 500 }
    );
  }

  const response = await fetch(`${API_BASE_URL}/api/demo/reset`, {
    method: "POST",
    headers: {
      "X-Demo-Token": demoResetToken,
    },
  });

  const data = await response.json();

  return NextResponse.json(data, {
    status: response.status,
  });
}