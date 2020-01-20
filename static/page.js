class Page {
    constructor(quill, token) {
        this.quill = quill;
        this.page_id = null;
        this.published = false;
        this.token = token;
        const page = this;

        quill.on("text-change", function(delta) {
            if (this.published) {

            }
        });

        const moveButton = setInterval(function () {
            if ($("div.ql-toolbar").length) {
                clearInterval(moveButton);
                $("div.ql-toolbar")[0].appendChild($("span.move")[0]);
                const publishButton = $("button#publish");
                const saveButton = $("button#save");
                publishButton.click(function() {
                    if (!page.published) {
                        page.publish(publishButton, saveButton);
                        publishButton.prop("disabled", true);
                        page.save();
                    } else {
                        window.open(window.location.href, "_blank");
                    }
                });
                saveButton.click(function() {
                    if (page.published) {
                        page.save();
                    }
                });
            }
        }, 5);
    }

    publish(publishButton, saveButton) {
        if (!this.published) {
            const self = this;
            $.get("/new").done(function(data) {
                self.update(data, true);
                history.pushState("editor", "Editor", "/" + self.page_id);
                publishButton.text(window.location.href);
                saveButton.css("visibility", "visible");
            });
        }
    }

    save() {
        if (this.published) {
            $.post("/save", {
                page: this.page_id,
                doc: JSON.stringify(this.quill.getContents()),
                csrfmiddlewaretoken: this.token,
            });
        }
    }

    update(page_id, published) {
        this.page_id = page_id;
        this.published = published;
    }
}