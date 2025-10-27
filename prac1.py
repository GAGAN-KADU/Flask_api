from flask import Flask,request
import json
app = Flask(__name__)

@app.route("/post",methods=["POST"])
def insert():
    data = request.get_json()
    with open("data.json","r") as f:
        try:
            content = json.load(f)
        except json.JSONDecodeError:
            content= []
    content.append(data)

    with open("data.json","w") as f:
        json.dump(content,f)


    return "Data Updated succesfully",201

@app.route("/patch/<int:user_id>",methods=["PATCH"])
def update_patch(user_id):
    data = request.get_json()
    new_username = data["username"]
    with open("data.json","r") as f:
        content = json.load(f)
    try:
        for  i in content:
            if user_id == i['id']:
                i['username'] = new_username

                break
    except:
        return "id not found"
    
    with open("data.json","w") as f:
        json.dump(content,f)
    
    return "Patch operation performed succesfully"

@app.route("/put/<int:user_id>",methods=["PUT"])
def update_put(user_id):
    new_data = {"id":"21","username":"new_put_record","pass":"pqrs"}
    with open("data.json","r") as f:
        content = json.load(f)
    print(content)
    try:
        for  i in content:
            if user_id == int(i['id']):
                i.update(new_data)
                break
            
    except:
        return "id not found"
    print(content)
    
    try:
        with open ("data.json","w") as f:
            json.dump(content,f)
    except json.JSONDecodeError:
        return "failed while updating"
    
    return "PUT succesfully performed"

    


@app.route("/get",methods = ['GET'])
def get_data():
    (user_id) = request.args.get('user_id')

    print ((user_id))
    with open("data.json","r") as f:
        content = json.load(f)
    print(content)

    try:
        for  i in content:
            id = i['id']
            print(id)
            if user_id == i['id']:
                return i
    except:
        return "id not found"
    
    return "pass"

@app.route("/delete/<int:user_id>",methods=["DELETE"])
def remove_data(user_id):
    print(user_id)
    print("change made to test new sencond test branch")
    with open("data.json","r") as f:
        content = json.load(f)
    for i in content:
        if user_id == int(i['id']):
            content.remove(i)
            break

    try:
        with open ("data.json","w") as f:
            json.dump(content,f)
    except json.JSONDecodeError:
        return "failed while deleting"
    
    return "delete succesfullly"



if __name__ == "__main__":
    app.run(debug="True")