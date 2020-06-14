const mongoose = require('mongoose');

const { Schema } = mongoose;

const logEntrySchema = new Schema({
    title: {
        type: String,
        required: true,
    },
    link: String,
    price: Number,
    description: String,
    image: String,
}, {
    timestamps: true,
});

const logEntry = mongoose.model('LogEntry', logEntrySchema);

module.exports = logEntry;

