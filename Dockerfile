# Stage 1: Build Stage (Installs dependencies)
FROM python:3.9-slim AS builder

# Set working directory
WORKDIR /app

# Copy script
COPY ip_tool.py .

# Install dependencies (if needed, but none required for now)
# RUN pip install -r requirements.txt

# Stage 2: Final Image (Minimal runtime)
FROM python:3.9-alpine

# Set working directory
WORKDIR /app

# Copy the built script from the builder stage
COPY --from=builder /app/ip_tool.py .

# Make the script executable
RUN chmod +x ip_tool.py

# Default command
ENTRYPOINT ["./ip_tool.py"]
