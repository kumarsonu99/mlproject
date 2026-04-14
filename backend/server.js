import express from "express";
import fetch from "node-fetch";
import cors from "cors";

const app = express();

app.use(cors());
app.use(express.json());

app.post("/check", async (req, res) => {
    const text = req.body.text;

    try {
        const response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text })
        });

        const data = await response.json();
        res.send(data);

    } catch (err) {
        res.status(500).send({ error: "ML server not running" });
    }
});

app.listen(3000, () => {
    console.log("Backend running on http://localhost:3000");
});