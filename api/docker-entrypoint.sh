#!/bin/bash

# Run migrations
piccolo migrations forwards app

# Execute the original command passed to the container (usually 'runserver')
exec "$@"