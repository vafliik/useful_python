# How to run Selenium grid

# Start the main "hub" instance
java -jar selenium-server-standalone.jar -role hub  # starts by default at http://localhost:4444


# On another host (can be the same), start the node - as much as you want
java -jar selenium-server-standalone.jar -role node -hub http://localhost:4444/grid/register   # starts by default at http://localhost:5555

# Then it is possible to check the status at http://localhost:4444/grid/console
# Sessions on individual nodes can be seen here: {node_url}/wd/hub