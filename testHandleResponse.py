import handleResponse as hr




response1 = {
  "status": {
      "timestamp": "2021-04-15T23:23:39.672Z",
      "error_code": 0,
      "error_message": None,
      "elapsed": 23,
      "credit_count": 1,
      "notice": None
  },
  "data": {
      "1": {
          "id": 1,
          "name": "Bitcoin",
          "symbol": "BTC",
          "slug": "bitcoin",
          "num_market_pairs": 9603,
          "date_added": "2013-04-28T00:00:00.000Z",
          "tags": [
              "mineable",
              "pow",
              "sha-256",
              "store-of-value",
              "state-channels",
              "coinbase-ventures-portfolio",
              "three-arrows-capital-portfolio",
              "polychain-capital-portfolio",
              "binance-labs-portfolio",
              "arrington-xrp-capital",
              "blockchain-capital-portfolio",
              "boostvc-portfolio",
              "cms-holdings-portfolio",
              "dcg-portfolio",
              "dragonfly-capital-portfolio",
              "electric-capital-portfolio",
              "fabric-ventures-portfolio",
              "framework-ventures",
              "galaxy-digital-portfolio",
              "huobi-capital",
              "alameda-research-portfolio",
              "a16z-portfolio",
              "1confirmation-portfolio",
              "winklevoss-capital",
              "usv-portfolio",
              "placeholder-ventures-portfolio",
              "pantera-capital-portfolio",
              "multicoin-capital-portfolio",
              "paradigm-xzy-screener"
          ],
          "max_supply": 21000000,
          "circulating_supply": 18683787,
          "total_supply": 18683787,
          "is_active": 1,
          "platform": None,
          "cmc_rank": 1,
          "is_fiat": 0,
          "last_updated": "2021-04-15T23:23:02.000Z",
          "quote": {
              "USD": {
                  "price": 76166.87047596426,
                  "volume_24h": 60941634537.86023,
                  "percent_change_1h": -0.45102232,
                  "percent_change_24h": 0.33035557,
                  "percent_change_7d": 9.22218571,
                  "percent_change_30d": 11.35482098,
                  "percent_change_60d": 28.8510739,
                  "percent_change_90d": 74.67035306,
                  "market_cap": 1180177669642.505,
                  "last_updated": "2021-04-15T23:23:02.000Z"
              }
          }
      }
  }
}

returnObject = hr.handleResponse(response1)
print(returnObject)