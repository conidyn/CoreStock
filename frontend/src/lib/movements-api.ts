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

export type CreateStockMovementPayload = {
  product_id: number;
  from_location_id: number;
  to_location_id: number;
  quantity: number;
  movement_type: "purchase" | "sale" | "transfer";
  reason: string;
};

export async function getStockMovements(): Promise<StockMovement[]> {
  const response = await fetch(`${API_BASE_URL}/api/stock-movements`);

  if (!response.ok) {
    throw new Error("Failed to fetch stock movements");
  }

  return response.json();
}

export async function getRecentStockMovements(
  limit = 5
): Promise<StockMovement[]> {
  const response = await fetch(
    `${API_BASE_URL}/api/stock-movements/recent?limit=${limit}`,
    {
      cache: "no-store",
    }
  );

  if (!response.ok) {
    throw new Error("Failed to fetch recent stock movements");
  }

  return response.json();
}

export async function createStockMovement(
  payload: CreateStockMovementPayload
): Promise<StockMovement> {
  const response = await fetch(`${API_BASE_URL}/api/stock-movements`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  if (!response.ok) {
    const errorData = await response.json();

    throw new Error(
      errorData.detail || "Failed to create stock movement"
    );
  }

  return response.json();
}