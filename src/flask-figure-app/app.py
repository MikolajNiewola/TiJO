from flask import Flask, render_template, request, jsonify
from figures import FigureService

app = Flask(__name__)
figure_service = FigureService()

@app.route('/')
def index():
    return render_template('index.html', figure_colors=figure_service.get_colors())

@app.route('/change-color', methods=['POST'])
def change_color():
    data = request.get_json()
    figure_type = data.get('figure_type')
    new_color = data.get('new_color')

    if figure_service.change_color(figure_type, new_color):
        return jsonify({"status": "success", "figure_colors": figure_service.get_colors()})
    return jsonify({"status": "error", "message": "figure type error"}), 400

@app.route('/change-color-all', methods=['POST'])
def change_color_all():
    data = request.get_json()
    new_color = data.get('new_color')

    if new_color:
        figure_service.change_color_all(new_color)
        return jsonify({"status": "success", "figure_colors": figure_service.get_colors()})
    return jsonify({"status": "error", "message": "new color error"}), 400

if __name__ == '__main__':
    app.run(debug=True)