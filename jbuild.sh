#! /bin/bash

#########################################
# Written by Jeff Huss for OS Docs team #
# Needs polishing but it's functional™  #
#########################################

# Installation Instuctions (bash only):
#   1) Place this file (jbuild.sh) in a local folder (such as ~/Documents as an example).
#          $ mv jbuild.sh ~/Documents
#   2) Change directories to the location of the script:
#          $ cd ~/Documents
#   2) Make this script executable by running the following command:
#          $ chmod 755 jbuild.sh
#   3) Verify that /usr/local/bin/ is part of your path by checking the output of the following command:
#          $ echo $PATH
#   4) If it isn't, add it:
#          $ export PATH="/usr/local/bin/:$PATH"
#   5) Create a symlink to the script in /usr/local/bin/ (this allows you to run the script from any directory):
#          $ sudo ln -s ~/Documents/jbuild.sh /usr/local/bin/jbuild
#          NOTE: Make sure to change the path to the script if it isn't in ~/Documents!
#   6) Navigate to the folder containing the page you would like to build and run the command "jbuild"
#          NOTE: Currently this can be used to build documentation-website and project-website. You may still
#                need to run "bundle install" if you haven't done so already. This requires manually adding a
#                line to the relevant Gemfile, (gem "webrick"), running "bundle install" from that directory,
#                and then proceeding with this script. When the script completes it will clean up any running
#                processes associated with the port you defined.

# Define a default port value
default_port=4000

# Initialize cport value
cport=($default_port)

# Add gem "webrick" to Gemfile
add_webrick()   {
    echo 'gem "webrick"' | tee -a Gemfile >/dev/null
}

# Remove gem "webrick" from Gemfile
remove_webrick()    {
    # Delete the line from the file
    sed -i '' '/gem "webrick"/d' Gemfile
    sed -i '' '/^.*webrick/d' Gemfile.lock
}

# Help message
help_text() {
    echo ""
    echo "Usage: This script will execute the following command:"
    echo ""
    echo "bundle exec jekyll serve --host localhost --port <port> --incremental --livereload --open-url"
    echo ""
    echo "There are 3 ways to use it:"
    echo ""
    echo "    1) Pass no arguments and the default port of $default_port will be used."
    echo "        $ jbuild"
    echo ""
    echo "    2) Pass a single, valid port number to serve the page from a custom port."
    echo "        $ jbuild 9001 "
    echo ""
    echo "    3) Pass -h or --help to see this text again."
    echo "        $ jbuild -h OR jbuild --help"
    echo ""
}

# Error text if port is in use
port_in_use_error()   {
        echo ""
        echo "Port $cport is in use. Please specify an unused port. You can use the following command to see if a specific port is open:"
        echo ""
        echo "    $ lsof -i:<port>"
        echo ""
        echo "Replace \"<port>\" with a valid port number. If the command does not return anything, the port is open."
        echo ""
}

# Gemfile error
gemfile_not_found() {
    echo "ERROR: Cannot locate Gemfile in this directory. Please make sure you are in the correct directory then rerun the script."
}

# The build command
jekyll_build()  {
    bundle exec jekyll serve --host localhost --port $cport --incremental --livereload --open-url
}

# Clean up ports after the script is run to prevent issues
port_clean_up() {
    for i in $(lsof -i:$cport -F 'p' | grep ^p | sed 's/p//g'); do
        kill $i
        done
}

# If the user passes "-h" or "--help" then display the help text
if [ "$1" = "-h" ] || [ "$1" = "--help" ]; then
   help_text
   exit 1
fi

# If the user passes too many arguments, report and display help text
if [ "$#" -gt 1 ]; then
    echo ""
    echo "=========================="
    echo "ERROR: Too many arguments!"
    echo "=========================="
    help_text
    exit 2
fi

# No args passed - check to see if the default port is open
if [ "$#" -eq 0 ]; then
    # Set port variable to default value since none was specified
    cport=($default_port)

    # This checks to see if a port is in use. It's lazy, but if any lines are returned
    # by lsor then it's safe to assume the port is being used and it shouldn't be built.
    if [ "$(lsof -i:$cport | wc -l)" -gt 0 ]; then
        port_in_use_error
        exit 2
    else
        # Check to see if you're in the correct directory - there needs to be a Gemfile present.
        if ! [ -e ./Gemfile ]; then
            gemfile_not_found
            exit 2
        fi
        # Since we know the Gemfile exists, let's make sure to add the webrick gem
        add_webrick
        # The default port is open AND bundle can find the Gemfile, so build it using the specified port
        jekyll_build
        # And since we don't want to accidentally commit anything with the webrick gem included, delete it
        remove_webrick
        # Clean up the port so the script can be run again
        port_clean_up
        exit 1
    fi
fi

# Single arg passed so we expect an integer that corresponds to a valid port number
if [ "$#" -eq 1 ]; then
    # Check to see if the input is an integer and that it is a valid port number
    if ! [[ "$1" =~ ^[0-9]+$ ]] || [ "$1" -gt 65535 ] || [ "$1" -lt 0 ]; then
        echo ""
        echo "===================="
        echo "ERROR: Invalid port!"
        echo "===================="
        help_text
        exit 2
    fi
    
    # Set custom port variable if the input was a valid port number
    cport=$1
    
    # This checks to see if a port is in use. It's lazy, but if any lines are returned
    # by lsof then it's safe to assume the port is being used and it shouldn't be built.
    if [ "$(lsof -i:$cport | wc -l)" -gt 0 ]; then
        port_in_use_error
        exit 2
    else
        # Check to see if you're in the correct directory - there needs to be a Gemfile present.
        if ! [ -e ./Gemfile ]; then
            gemfile_not_found
            exit 2
        fi
        # Since we know the Gemfile exists, let's make sure to add the webrick gem
        add_webrick
        # The default port is open AND bundle can find the Gemfile, so build it using the specified port
        jekyll_build
        # And since we don't want to accidentally commit anything with the webrick gem included, delete it
        remove_webrick
        # Clean up the port so the script can be run again
        port_clean_up
        exit 1
    fi
fi