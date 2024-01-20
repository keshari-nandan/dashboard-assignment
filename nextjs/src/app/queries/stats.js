
const totalSpend = {
    "measures": [
      "expenses.total"
    ],
    "timeDimensions": [
      {
        "dimension": "expenses.date",
        "granularity": "month",
        "dateRange": "This month"
      }
    ]
  }


  const totalSpendByCards = {
    "measures": [
      "expenses.total"
    ],
    "timeDimensions": [
      {
        "dimension": "expenses.date",
        "granularity": "month",
        "dateRange": "This month"
      }
    ],
    "filters": [
      {
        "member": "expenses.payment_mode",
        "operator": "contains",
        "values": [
          "CARD"
        ]
      }
    ]
  }

  const totalInventment = {
    "measures": [
      "expenses.total"
    ],
    "timeDimensions": [
      {
        "dimension": "expenses.date",
        "granularity": "month",
        "dateRange": "This month"
      }
    ],
    "filters": [
      {
        "member": "categories.name",
        "operator": "contains",
        "values": [
          "investment"
        ]
      }
    ]
  }

  const totalGroceries = {
    "measures": [
      "expenses.total"
    ],
    "timeDimensions": [
      {
        "dimension": "expenses.date",
        "granularity": "month",
        "dateRange": "This month"
      }
    ],
    "filters": [
      {
        "member": "categories.name",
        "operator": "contains",
        "values": [
          "groceries"
        ]
      }
    ]
  }