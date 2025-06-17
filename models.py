from dataclasses import dataclass

@dataclass
class Product:
    id: int
    brand: str
    model: str
    price_value: str
    currency: str
    country_origin: str
    color: str
    weight_g: str
    product_code: str

    @classmethod
    def init(cls, data: dict) -> 'Product':
        id=data.get('id'),
        data = cls.parse_data(data.get('description'))
        return cls(id=id, **data)
    
    @staticmethod
    def extract_field(data: str, key: str, end: str = '.') -> str:
        try:
            return data.split(key)[1].split(end)[0].strip()
        except IndexError:
            return 'Not specified'
    
    @staticmethod
    def parse_data(data: str) -> dict:
        fields = {}
        temp = data.split(' ')
        print(temp)
        fields['brand'] = data.split('model')[0].strip('.')
        fields['model'] = temp[temp.index('model') + 1].strip('.')
        fields['price_value'] = Product.extract_field(data, 'Price:') if 'none' not in Product.extract_field(data, 'Price:').lower() else 'none'
        fields['currency'] = temp[temp.index('Price:') + 2].strip('.') if temp[temp.index('Price:') + 2] != '.' else 'Not specified'
        fields['country_origin'] = Product.extract_field(data, 'Origin:')
        fields['color'] = Product.extract_field(data, 'Color:')
        fields['weight_g'] = Product.extract_field(data, 'Weight:').split(' ')[0] if 'Weight:' in data else 'Not specified'
        fields['product_code'] = Product.extract_field(data, 'Code:')
        return fields
