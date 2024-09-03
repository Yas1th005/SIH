// Backend code remains the same
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');

const app = express();
const PORT = 5000; // Backend server port

app.use(cors()); // Enable CORS
app.use(express.json()); // Parse JSON data

// MongoDB connection
mongoose.connect('mongodb://localhost:27017/sih-data', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

const db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', () => {
  console.log('Connected to MongoDB');
});

// Define a Mongoose schema and model for your data
const DataSchema = new mongoose.Schema({
  Category: String,
  Description: String,
  Location: String
});

const DataModel = mongoose.model('news', DataSchema);

// API endpoint to fetch data from MongoDB
app.get('/news', async (req, res) => {
  try {
    const data = await DataModel.find(); // Fetch all documents from the collection
    res.json(data); // Send data as JSON
    console.log("sent")
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
