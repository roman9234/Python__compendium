import json
import xml.etree.ElementTree as ET


from flask import Flask, request


app = Flask(__name__)


@app.route("/")
def hello_world():
   return "<p>Работает</p>"




@app.post("/api/v1/json/order")
def post_json_order():
   try:
       client = request.json.get("client")
       if client is None:
           return "client не передан или передан не корректно", 400


       products = request.json.get("products")
       if products is None or not isinstance(products, list):
           return "products не передан или передан не корректно", 400


       product_names = set()
       total = 0
       for p in products:
           product_names.add(p.get('name'))
           total += p.get('price')


       voucher = request.json.get("voucher")
       if voucher is None:
           return "voucher не передан или передан не корректно", 400


       discount = voucher.get("discount")
       if not discount or not discount.endswith("%"):
           return "discount не передан или передан не корректно", 400


       discount = int(discount[:-1])
       print(discount)
       print(total)
       total = total - total * discount / 100


       return json.dumps(dict(
           client=client,
           total=total,
           products=list(product_names)
       ))
   except Exception as e:
       return str(e), 500




@app.post("/api/v1/xml/order")
def post_xml_order():
   try:
       root = ET.fromstring(request.data)
       if root.tag != 'order':
           return "не верный корневой тег", 400


       client = root.get('client')
       if not client:
           return "client не передан или передан не корректно", 400




       product_names = set()
       total = 0
       discount = None
       for p in root:
           if p.tag == 'product':
               product_names.add(p.get('name'))
               total += int(p.get('price'))


           if p.tag == 'discount':
               if not p.text.endswith('%'):
                   return 'discount был передан некорректно', 400


               discount = int(p.text[:-1])
       total = total - total * discount / 100
       product_names = list(product_names)


       xml = ET.Element("order", total=str(int(total)), products=",".join(product_names), client=client)
       return ET.tostring(xml, encoding='unicode')
   except Exception as e:
       return str(e), 500


if __name__ == "__main__":
    app.run(debug=True)