import { API_BASE_URL } from "@/config/api";

export type StockLocation = {
  id: number;
  name: string;
  type: "internal" | "supplier" | "customer";
};

export async function getStockLocations(): Promise<StockLocation[]> {
  const response = await fetch(`${API_BASE_URL}/api/stock-locations`);

  if (!response.ok) {
    throw new Error("Failed to fetch stock locations");
  }

  return response.json();
}