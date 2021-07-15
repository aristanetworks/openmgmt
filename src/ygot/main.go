package main

import (
	"fmt"
	"log"
	"os"

	oc "github.com/aristanetworks/openmgmt/src/ygot/pkg"
	"github.com/openconfig/ygot/ygot"
)

func main() {
	h := &oc.System{Hostname: ygot.String("ceos1")}
	d := &oc.Device{System: h}

	json, err := ygot.EmitJSON(d, &ygot.EmitJSONConfig{
		Format: ygot.RFC7951,
		Indent: "  ",
		RFC7951Config: &ygot.RFC7951JSONConfig{
			AppendModuleName: true,
		},
	})
	if err != nil {
		panic(fmt.Sprintf("JSON demo error: %v", err))
	}
	fmt.Println("This is the output")
	fmt.Println(json)
	fmt.Println("Adding to config/hostname.json")

	f, err := os.Create("config/hostname.json")

	if err != nil {
		log.Fatal(err)
	}

	defer f.Close()

	f.WriteString(json)

}
