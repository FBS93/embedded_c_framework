package filemerge

import (
	"os"
	"path/filepath"
	"runtime"
	"testing"
)

func TestWriteFileAtomicReadOnlyDir(t *testing.T) {
	if runtime.GOOS == "windows" {
		t.Skip("chmod 555 semantics differ on Windows")
	}
	// Simulate a directory that was created with read-only permissions (555),
	// as may happen when a previous installer version or the AI agent itself
	// creates the skills directory.
	base := t.TempDir()
	skillDir := filepath.Join(base, "sdd-init")
	if err := os.Mkdir(skillDir, 0o555); err != nil {
		t.Fatalf("Mkdir() error = %v", err)
	}

	path := filepath.Join(skillDir, "SKILL.md")
	content := []byte("# SDD Init\n")

	result, err := WriteFileAtomic(path, content, 0o644)
	if err != nil {
		t.Fatalf("WriteFileAtomic() on read-only dir error = %v", err)
	}
	if !result.Changed || !result.Created {
		t.Fatalf("WriteFileAtomic() result = %+v, want Changed=true Created=true", result)
	}

	got, err := os.ReadFile(path)
	if err != nil {
		t.Fatalf("ReadFile() error = %v", err)
	}
	if string(got) != string(content) {
		t.Fatalf("file content = %q, want %q", got, content)
	}
}

func TestWriteFileAtomicCreatesAndIsIdempotent(t *testing.T) {
	dir := t.TempDir()
	path := filepath.Join(dir, "nested", "config.json")
	content := []byte("{\"ok\":true}\n")

	first, err := WriteFileAtomic(path, content, 0o644)
	if err != nil {
		t.Fatalf("WriteFileAtomic() first write error = %v", err)
	}

	if !first.Changed || !first.Created {
		t.Fatalf("WriteFileAtomic() first write result = %+v", first)
	}

	second, err := WriteFileAtomic(path, content, 0o644)
	if err != nil {
		t.Fatalf("WriteFileAtomic() second write error = %v", err)
	}

	if second.Changed || second.Created {
		t.Fatalf("WriteFileAtomic() second write result = %+v", second)
	}

	got, err := os.ReadFile(path)
	if err != nil {
		t.Fatalf("ReadFile() error = %v", err)
	}

	if string(got) != string(content) {
		t.Fatalf("file content = %q", string(got))
	}
}
