import { API_BASE_URL } from "@/config/api";

export type MovementProduct = {
  id: number;
  name: string;
  sku: string;
};

export type MovementLocation = {
  id: number;
  name: string;
  type: string;
};

export type StockMovement = {
  id: number;
  quantity: number;
  movement_type: "purchase" | "sale" | "transfer";
  reason: string;
  created_at: string;
  product: MovementProduct;
  from_location: MovementLocation;
  to_location: MovementLocation;
};

export async function getStockMovements(): Promise<StockMovement[]> {
  const response = await fetch(`${API_BASE_URL}/api/stock-movements`);

  if (!response.ok) {
    throw new Error("Failed to fetch stock movements");
  }

  return response.json();
}