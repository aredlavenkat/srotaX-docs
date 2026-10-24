#!/bin/sh
set -eu
backend=${SROTAX_BACKEND_DIR:-../srotax-backend}
java=${JAVA_HOME:?Set JAVA_HOME to JDK 21}/bin/java
classpath="$backend/srotax-management-app/target/test-classes:$backend/srotax-management-app/target/classes:$backend/srotax-api-contract/target/classes:$backend/srotax-core/target/classes:$backend/srotax-engine-adapter/target/classes:$backend/srotax-compiler/target/classes:$(cat "$backend/srotax-management-app/target/browser-classpath.txt")"
"$java" -cp "$classpath" scripts/VerifyExpressions.java
