from flask import Flask, jsonify, request
import random
import string

app = Flask(__name__)

# دالة لتوليد كود جوجل بلاي عشوائي
def generate_play_code(length=4):
    code = ""
    for _ in range(length):
        part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        code += part + "-"
    return code.rstrip("-")

# دالة لتوليد عدة أكواد
def generate_multiple_codes(count, length=4):
    codes = []
    for _ in range(count):
        codes.append(generate_play_code(length))
    return codes

# مسار API لتوليد عدد من أكواد جوجل بلاي
@app.route('/generate_code', methods=['GET'])
def generate_code():
    # الحصول على عدد الأكواد وطول الأجزاء من المعاملات في الرابط
    count = int(request.args.get('count', 1))  # إذا لم يتم تحديد عدد الأكواد، يتم توليد كود واحد
    length = int(request.args.get('length', 4))  # طول الأجزاء (عدد الأحرف في كل جزء)
    
    # توليد الأكواد
    codes = generate_multiple_codes(count, length)
    return jsonify({"play_codes": codes})

if __name__ == '__main__':
    app.run(debug=True)
