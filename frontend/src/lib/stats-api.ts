import { API_BASE_URL } from "@/config/api";

export type MovementBreakdown = {
  purchase: number;
  transfer: number;
  sale: number;
};

export type DashboardStats = {
  total_products: number;
  total_stock_quantity: number;
  low_stock_count: number;
  total_movements: number;
  movement_breakdown: MovementBreakdown;
};

export async function getDashboardStats(): Promise<DashboardStats> {
  const response = await fetch(`${API_BASE_URL}/api/stats/dashboard`);

  if (!response.ok) {
    throw new Error("Failed to fetch dashboard stats");
  }

  return response.json();
}