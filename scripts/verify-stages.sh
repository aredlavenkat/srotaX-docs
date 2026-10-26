#!/bin/sh
set -eu
core=${FLUXION_CORE_DIR:-../fluxion-core-engine}
java=${JAVA_HOME:?Set JAVA_HOME to JDK 21}/bin/java
classpath="$core/target/classes:$(cat "$core/target/docs-classpath.txt")"
"$java" -cp "$classpath" scripts/VerifyStages.java "$@"
