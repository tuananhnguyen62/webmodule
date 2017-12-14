from flask import Flask, render_template, request, flash
import mlab
from mongoengine import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "Csb~a J]?E3z_mx"
#1. Connect to database
mlab.connect()

#2. Design collection
class Item(Document):
    title = StringField()
    image = StringField()
    description = StringField()
    price = IntField()

#3. Try to insert an item
# tv = Item(
#     title = "Đồng hồ cổ",
#     image = "http://3.bp.blogspot.com/-ab1m4HqFjMw/UI67mvM8eTI/AAAAAAAAcBU/u9_R97TsDc8/s400/mr_869031_4f0ec9fcc26125d3.jpg",
#     description = "Âm-li từ thập niên 90",
#     price = 4000000,
# )
# tv.save()
# items = Item.objects()
# for item in items:
#     print(item.title)


@app.route('/')
def index():
    items = Item.objects() # Get ALL items
    return render_template('index.html', items=items)


@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    if request.method == "GET": # Get form
        return render_template('add_item.html')
    elif request.method == "POST": # Receive form
        # 1 Extract data in form
        form = request.form
        title = form['title']
        image = form['image']
        description = form['description']
        price = form['price']

        # 2 Add into database
        new_item = Item(title=title, image=image, description=description, price=price)
        new_item.save() # Save into database

        return "OKe anh"

@app.route('/admin')
def admin():
    return render_template('admin.html', items=Item.objects())

@app.route('/edit_item/<item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    item = Item.objects().with_id(item_id)
    if request.method == "GET":
        return render_template('edit_item.html', item= item)
    elif request.method == "POST":
        form = request.form
        title = form['title']
        description = form['description']
        image = form['image']
        price = form['price']

        item.update(title=title, description=description, image=image, price=price)

        flash("Updated successfully")

        return render_template('edit_item.html', item= Item.objects().with_id(item_id))

@app.route('/delete_item/<item_id>', methods=['GET', 'POST'])
def delete_item(item_id):
    item = Item.objects().with_id(item_id)
    if request.method == "GET":
        return render_template('delete_item.html', item= item)
    if request.method == "POST":
        item.delete()
        return render_template('admin.html', items=Item.objects())

if __name__ == '__main__':
  app.run(debug=True)
