#!/usr/bin/env python3
"""
Jungle Scout vs Helium 10 Seller Cost & Multi-Seat Calculator 2026.
"""
import argparse

def calculate(seats, annual):
    # Jungle Scout Suite: $49/mo annual ($588/yr) or $69/mo monthly. Additional seat: $450/yr or $49/mo
    js_base = 588.0 if annual else (69.0 * 12.0)
    js_extra_seats = max(0, seats - 1) * (450.0 if annual else (49.0 * 12.0))
    js_total = js_base + js_extra_seats

    # Helium 10 Platinum: $948/yr annual or $99/mo monthly (single user). Diamond for multi-user: $2,748/yr or $279/mo
    if seats > 1:
        h10_total = 2748.0 if annual else (279.0 * 12.0)
    else:
        h10_total = 948.0 if annual else (99.0 * 12.0)

    diff = h10_total - js_total

    print("=" * 60)
    print("Amazon FBA Suite Comparison: Jungle Scout vs Helium 10")
    print("=" * 60)
    print(f"Team Seats:              {seats}")
    print(f"Billing Term:            {'Annual Prepaid' if annual else 'Monthly'}")
    print(f"Jungle Scout Suite:      ${js_total:.2f}/year (${(js_total/12):.2f}/mo)")
    if seats > 1:
        print(f"Helium 10 Diamond:       ${h10_total:.2f}/year (${(h10_total/12):.2f}/mo)")
    else:
        print(f"Helium 10 Platinum:      ${h10_total:.2f}/year (${(h10_total/12):.2f}/mo)")
    print(f"Cost Difference:         ${abs(diff):.2f}/year ({'JS Cheaper' if diff > 0 else 'H10 Cheaper'})")
    print("=" * 60)
    return js_total, h10_total

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Jungle Scout vs Helium 10")
    parser.add_argument("--seats", type=int, default=1)
    parser.add_argument("--annual", action="store_true", default=True)
    args = parser.parse_args()
    calculate(args.seats, args.annual)
