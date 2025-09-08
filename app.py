from flask import Flask, render_template, Response
import matplotlib
matplotlib.use('Agg')  # important fix
import matplotlib.pyplot as plt
import numpy as np
import io


app = Flask(__name__)

# ==== Data ====
shoes = {
    'Crocks': 300,
    'Slippers': 150,
    'Samba': 2000,
    'Air Force': 1500
}
h = np.random.random(1000)  # histogram data
n = np.linspace(0, 10, 100) # line data


# ==== Helper to convert plot to PNG ====
def plot_to_png():
    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    return buf


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/hist")
def hist_plot():
    fig, ax = plt.subplots()
    ax.hist(h, bins=30, color="skyblue", edgecolor="black")
    ax.set_title("Histogram of Random Numbers")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")

    buf = plot_to_png()
    plt.close(fig)
    return Response(buf.getvalue(), mimetype="image/png")


@app.route("/line")
def line_plot():
    fig, ax = plt.subplots()
    ax.plot(n, np.exp(n), color="green", linewidth=2)
    ax.set_title("Exponential Line Plot")
    ax.set_xlabel("n")
    ax.set_ylabel("exp(n)")

    buf = plot_to_png()
    plt.close(fig)
    return Response(buf.getvalue(), mimetype="image/png")


@app.route("/bar")
def bar_plot():
    fig, ax = plt.subplots()
    ax.bar(shoes.keys(), shoes.values(), color="orange")
    ax.set_title("Shoes Prices")
    ax.set_xlabel("Type of Shoe")
    ax.set_ylabel("Price")

    buf = plot_to_png()
    plt.close(fig)
    return Response(buf.getvalue(), mimetype="image/png")


@app.route("/scatter")
def scatter_plot():
    fig, ax = plt.subplots()
    ax.scatter([1, 3, 5, 7], [3, 2, 6, 4], color="red", s=100)
    ax.set_title("Scatter Plot Example")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    buf = plot_to_png()
    plt.close(fig)
    return Response(buf.getvalue(), mimetype="image/png")


if __name__ == "__main__":
    app.run(debug=True)
