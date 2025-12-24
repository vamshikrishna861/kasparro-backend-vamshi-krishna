# Kasparro Backend & ETL Assignment

This project is a backend and ETL-style application built using FastAPI.  
It fetches cryptocurrency market data from public APIs and exposes them via REST endpoints.  
The application is containerized using Docker.

## Tech Stack
- Python
- FastAPI
- Requests
- Uvicorn
- Docker

## Data Sources
- CoinGecko API
- CoinPaprika API

## API Endpoints

GET /

GET /prices

## Run with Docker

docker build -t kasparro-backend .

docker run -p 8000:8000 kasparro-backend

## Author
Vamshi Krishna
