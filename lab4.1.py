from datetime import datetime

def generate_tracking_update(status, order_id="ORD-1001", customer="Customer"):
    status = status.strip().lower()

    updates = {
        "pending": {
            "title": "Order Pending",
            "message": (
                f"Hi {customer}, your order {order_id} has been received and is "
                "currently pending processing. We'll notify you once it moves to "
                "the next stage."
            )
        },
        "processing": {
            "title": "Order Processing",
            "message": (
                f"Hi {customer}, your order {order_id} is now being processed "
                "at our fulfillment center. It will be prepared for dispatch soon."
            )
        },
        "shipped": {
            "title": "Order Shipped",
            "message": (
                f"Hi {customer}, great news! Your order {order_id} has been shipped "
                "and is currently in transit. You can expect further tracking "
                "updates as it moves through the delivery network."
            )
        },
        "out_for_delivery": {
            "title": "Out for Delivery",
            "message": (
                f"Hi {customer}, your order {order_id} is out for delivery today. "
                "Please keep an eye out for the delivery."
            )
        },
        "delivered": {
            "title": "Order Delivered",
            "message": (
                f"Hi {customer}, your order {order_id} has been successfully "
                "delivered. We hope you enjoy your purchase!"
            )
        },
        "cancelled": {
            "title": "Order Cancelled",
            "message": (
                f"Hi {customer}, your order {order_id} has been cancelled. "
                "If you believe this was unexpected, please contact customer support."
            )
        }
    }

    if status not in updates:
        return {
            "status": "error",
            "message": (
                f"Unknown status '{status}'. Supported statuses: "
                f"{', '.join(updates.keys())}"
            )
        }

    update = updates[status]

    return {
        "status": status,
        "order_id": order_id,
        "customer": customer,
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "title": update["title"],
        "tracking_message": update["message"]
    }


# Simulation
statuses = ["pending", "processing", "shipped",
            "out_for_delivery", "delivered"]

for status in statuses:
    result = generate_tracking_update(
        status,
        order_id="ORD-2026-8472",
        customer="Alex"
    )

    print(f"\n[{result['title']}]")
    print(result["tracking_message"])
