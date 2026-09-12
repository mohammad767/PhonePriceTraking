def clean_price(price) : 
    try : 
        cleaned_price = int(price.replace("تومان", "").replace(",", "").strip())
        return cleaned_price
    
    except (ValueError, AttributeError):
        return None

