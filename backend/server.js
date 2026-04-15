import express from "express";
import fetch from "node-fetch";
import cors from "cors";

const app = express();

app.use(cors());
app.use(express.json());

app.post("/check", async (req, res) => {
  const text = req.body.text;

  if (!text) {
    return res.status(400).json({ error: "No text provided" });
  }

  try {
    // First check ML health
    const healthRes = await fetch("http://127.0.0.1:5000/health");
    const healthData = await healthRes.json();
    
    if (healthData.status !== 'ok') {
      return res.status(503).json({ error: "ML service unhealthy - model load failed" });
    }

    const response = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ text })
    });

    const data = await response.json();

    console.log("🔍 ML RAW RESPONSE:", data);

    // 🔥 Handle ALL possible ML formats
    let result;

    if (typeof data.result === "string") {
      // Case: { result: "Toxic" }
      result = data.result;

    } else if (typeof data.prediction === "string") {
      // Case: { prediction: "Toxic" }
      result = data.prediction;

    } else if (typeof data.prediction === "number") {
      // Case: { prediction: 1 }
      result = data.prediction === 1 ? "Toxic" : "Not Toxic";

    } else if (typeof data.label === "number") {
      // Case: { label: 1 }
      result = data.label === 1 ? "Toxic" : "Not Toxic";

    } else {
      // Unknown format
      result = "Not Toxic";
    }

    res.json({ result });

  } catch (err) {
    console.error("❌ ERROR:", err.message);
    res.status(500).json({ error: "ML server not available (not started?)" });
  }
});

app.listen(3000, '0.0.0.0', () => {
  console.log("🚀 Backend running on http://localhost:3000");
});
