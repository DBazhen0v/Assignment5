deposit_account = {
"client_id": "C1025",
"balance": 5000.0,
"currency": "UAH",
"interest_rate": 0.08, # 8% річних
"is_active": True
}
summ = deposit_account["balance"] * deposit_account["interest_rate"]

print("Нараховані відсотки за рік", summ)
deposit_account["balance"] = deposit_account["balance"] * 0.08
deposit_account["last_update_type"] = "interest accrual"
deposit_account["is_active"] = False
print(deposit_account)




