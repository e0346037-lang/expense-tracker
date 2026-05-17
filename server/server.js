const express = require('express');
const mongoose = require('mongoose');
const app = express();

app.use(express.json());

app.get('/', (req, res) => {
    res.send("Expense Tracker Backend is Running!");
});

const PORT = 5000;
app.listen(PORT, () => {
console.log(`(server started on port ${PORT}`);