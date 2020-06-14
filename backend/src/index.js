const express = require('express');
const morgan = require('morgan');
const helmet = require('helmet');
const cors = require('cors');
const mongoose = require('mongoose');

require('dotenv').config();

const middlewares = require('./middlewares');
const logs = require('./api/logs');

mongoose.connect(process.env.DATABASE_URL, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
});

const { connection: db } = mongoose;

db.on('connected', () => {
    console.log('Database connected');
});

db.on('disconnected', () => {
    console.log('Database disconnected');
});

db.on('error', err => {
    console.error(err);
});

const port = process.env.PORT;
const app = express()
    .use(helmet())
    .use(morgan('common'))
    .use(cors({
        origin: `http://localhost:3000`,
    }))
    .use(express.json());

app.get('/', (req, res) => {
    res.json({
        'message': 'PriceTracker',
    });
});

app.use('/api/logs', logs);

app.use(middlewares.notFound);
app.use(middlewares.errorHandler);

app.listen(port, () => {
    console.log(`API listening at http://localhost:${port}`);
});
