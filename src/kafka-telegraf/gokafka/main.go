package main

import (
	"context"
	"flag"
	"fmt"
	"os"
	"os/signal"
	"strings"
	"syscall"
	"time"

	//"github.com/namsral/flag"
	"github.com/rs/zerolog/log"
	kafka "github.com/segmentio/kafka-go"
)

var (
	// kafka
	kafkaBrokerUrl     string
	kafkaVerbose       bool
	kafkaTopic         string
	kafkaConsumerGroup string
	kafkaClientId      string
	kafkaTime          int
)

func main() {
	flag.StringVar(&kafkaBrokerUrl, "kafka-brokers", "localhost:19092,localhost:29092,localhost:39092", "Kafka brokers in comma separated value")
	flag.BoolVar(&kafkaVerbose, "kafka-verbose", true, "Kafka verbose logging")
	flag.StringVar(&kafkaTopic, "kafka-topic", "foo", "Kafka topic. Only one topic per worker.")
	flag.StringVar(&kafkaConsumerGroup, "kafka-consumer-group", "consumer-group", "Kafka consumer group")
	flag.StringVar(&kafkaClientId, "kafka-client-id", "my-client-id", "Kafka client id")
	flag.IntVar(&kafkaTime, "kafka-time", 1, "Time to wait between updates there is no default if not selected")

	flag.Parse()

	sigchan := make(chan os.Signal, 1)
	signal.Notify(sigchan, syscall.SIGINT, syscall.SIGTERM)

	brokers := strings.Split(kafkaBrokerUrl, ",")

	// make a new reader that consumes from topic-A
	config := kafka.ReaderConfig{
		Brokers:         brokers,
		GroupID:         kafkaClientId,
		Topic:           kafkaTopic,
		MinBytes:        10e3,            // 10KB
		MaxBytes:        10e6,            // 10MB
		MaxWait:         1 * time.Second, // Maximum amount of time to wait for new data to come when fetching batches of messages from kafka.
		ReadLagInterval: -1,
	}

	reader := kafka.NewReader(config)
	defer reader.Close()

	for {
		if kafkaTime != 0 {
			time.Sleep(time.Duration(kafkaTime) * time.Second)
		}
		m, err := reader.ReadMessage(context.Background())
		if err != nil {
			log.Error().Msgf("error while receiving message: %s", err.Error())
			continue
		}

		value := m.Value
		//if m.CompressionCodec == snappy.NewCompressionCodec() {
		//	_, err = snappy.NewCompressionCodec().Decode(value, m.Value)
		//}

		if err != nil {
			log.Error().Msgf("error while receiving message: %s", err.Error())
			continue
		}

		fmt.Printf("message at topic/partition/offset %v/%v/%v: %s\n", m.Topic, m.Partition, m.Offset, string(value))
	}
}
