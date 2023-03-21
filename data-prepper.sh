#! /bin/bash

# Start the Fluent Bit container
init_fluent_bit() {
    docker run -d \
        -v fluent-bit.conf:/fluent-bit/etc/fluent-bit.conf -v 
}

# Write the default config for Fluent Bit
write_fluent_bit_conf()	{
	cat <<- 'EOF' > fluent-bit.conf
}