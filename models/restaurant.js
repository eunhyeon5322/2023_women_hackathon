// models/restaurant.js

const mongoose = require('mongoose');

const restaurantSchema = new mongoose.Schema({
  name: { type: String, required: true },
  description: { type: String },
  address: { type: String },
  phone: { type: String },
});

module.exports = mongoose.model('Restaurant', restaurantSchema);
