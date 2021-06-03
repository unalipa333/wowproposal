import handleResponse as hr




response1 = {
    "status": {
        "timestamp": "2021-05-28T00:15:58.844Z",
        "error_code": 0,
        "error_message": None,
        "elapsed": 19,
        "credit_count": 1,
        "notice": None
    },
    "data": {
        "1027": {
            "id": 1027,
            "name": "Ethereum",
            "symbol": "ETH",
            "slug": "ethereum",
            "num_market_pairs": 5991,
            "date_added": "2015-08-07T00:00:00.000Z",
            "tags": [
                "mineable",
                "pow",
                "smart-contracts",
                "ethereum",
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
                "hashkey-capital-portfolio",
                "kinetic-capital",
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
            "max_supply": None,
            "circulating_supply": 116051687.374,
            "total_supply": 116051687.374,
            "is_active": 1,
            "platform": None,
            "cmc_rank": 2,
            "is_fiat": 0,
            "last_updated": "2021-05-28T00:15:02.000Z",
            "quote": {
                "USD": {
                    "price": 2734.813923717091,
                    "volume_24h": 33061273564.05375,
                    "percent_change_1h": -0.79315057,
                    "percent_change_24h": -4.26155765,
                    "percent_change_7d": -3.21113596,
                    "percent_change_30d": 1.68082176,
                    "percent_change_60d": 61.64390186,
                    "percent_change_90d": 87.10258977,
                    "market_cap": 317379770501.2781,
                    "last_updated": "2021-05-28T00:15:02.000Z"
                }
            }
        }
    }
}

returnObject = hr.handleResponse(response1)
print(returnObject)