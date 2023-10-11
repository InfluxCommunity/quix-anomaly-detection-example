# Quix Machine Anomaly Detection

This project provides an example of how to use [Quix](https://quix.io) and InfluxDB 3.0 to build a machine anomaly detection data pipeline. This repository contains the full data pipeline as a project but does not include the data simulator (See getting started for more details).

## Prerequisites
* Sign up for a [Quix](https://quix.io) account
* Sign up for a [InfluxDB Cloud 3.0](https://cloud2.influxdata.com/signup) account
* Download and run the simulator from [here](https://github.com/InfluxCommunity/Arrow-Task-Engine/tree/hivemq)


## Getting Started
1. Fork this repository
2. Log into your Quix account.

3. Click `+ Create project`.

4. Give your project a name. For example, "Anomaly Detection".

5. Select `Connect to your own Git repo`, and follow the setup guide for your provider.
   
6. Assuming you are connecting to a GitHub account, you'll now need to copy the SSH key provided by Quix into your GitHub account. See the setup guide for further details.

7. Click Validate to test the connection between Quix and GitHub.

8. Click Done to proceed.

9. You will need to check the enviroment varibles for each stage of the Data Pipeline and modify them to connect to your own InfluxDB instance.

## Running the simulator
1. Clone the simulator from [here](https://github.com/InfluxCommunity/Arrow-Task-Engine/tree/hivemq)
```bash
git clone https://github.com/InfluxCommunity/Arrow-Task-Engine/tree/hivemq
```
2. cd into the directory and run the simulator using `docker compose`

```bash
docker compose up -d
```
**Note this will write the simulated data to the public HiveMQ broker. You may want to modify this and the Quix data pipeline to point at your own.**