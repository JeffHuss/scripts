#! /bin/bash

# Write the default config for Fluent Bit
write_fluent_bit_conf()	{
    echo "Writing Fluent Bit config file..."
	cat <<- ''EOF' > fluent-bit.conf
    [INPUT]
        name                  tail
        refresh_interval      5
        path                  /var/log/test.log
        read_from_head        true

    [OUTPUT]
        Name http
        Match *
        Host data-prepper
        Port 2021
        URI /log/ingest
        Format json
    EOF
}

# Create test log file
init_test_log() {
    echo "Initializing test log file..."
    touch test.log
}

# Start the Fluent Bit container
init_fluent_bit() {
    echo "Launching Fluent Bit container..."
    docker run -d \
        -v fluent-bit.conf:/fluent-bit/etc/fluent-bit.conf \
        -v test.log:/var/log/test.log \
        --network opensearch-net
}

