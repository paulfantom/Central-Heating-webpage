;
(function () {
    var $ = window.jQuery,
        $win = $(window),
        $doc = $(document),
        $body;

    // Listen touch events in touch screen device, instead of mouse events in desktop.
    var touchSupported = 'ontouchstart' in window,
        mousedownEvent = 'mousedown' + (touchSupported ? ' touchstart' : ''),
        mousemoveEvent = 'mousemove.plusminus' + (touchSupported ? ' touchmove.clockpicker' : ''),
        mouseupEvent = 'mouseup.plusminus' + (touchSupported ? ' touchend.plusminus' : '');

    // Get a unique id
    var idCounter = 0;

    function uniqueId(prefix) {
        var id = ++idCounter + '';
        return prefix ? prefix + id : id;
    }

    // Popover template
    var tpl = [
        '<div class="popover plusminus-popover">',
          '<div class="arrow"></div>',
            '<div class="popover-title">',
               '<span class="plusminus-span-value text-primary"></span>',
               ' &deg;C',
             '</div>',
             '<div class="plusminus-content">',
               '<div class="btn-group">',
               '</div>',
             '</div>',
           '</div>'].join('');

    // PlusMinus
    function PlusMinus(element, options) {
        var popover = $(tpl),
            isInput = element.prop('tagName') === 'INPUT',
            input = isInput ? element : element.find('input'),
            btnGroup = popover.find('.btn-group'),
            self = this;
        
        this.id = uniqueId('pm');
        this.element = element;
        this.options = options;
        this.input = input;
        this.isInput = isInput;
        this.popover = popover;
        this.isShown = false;
        this.isAppended = false;
        this.btnGroup = btnGroup;
        this.spanValue = popover.find('.plusminus-span-value');
        
        $('.plusminus-span-value').empty().append(this.input.val());

        if ((options.placement === 'top' || options.placement === 'bottom') && (options.align === 'top' || options.align === 'bottom')) options.align = 'left';
	if ((options.placement === 'left' || options.placement === 'right') && (options.align === 'left' || options.align === 'right')) options.align = 'top';
        
        $('<button type="button" class="btn btn-info plusminus-minus"><span class="glyphicon glyphicon-minus"></span></button>').on("click", function() {
            self.value = humanize(parseFloat(self.value) - options.step,options.precision);
            if (parseFloat(self.value) < parseFloat(options.min)){
                self.value = options.min;
            }
            $('.plusminus-span-value').empty().append(self.value);
        }).appendTo(this.btnGroup);
            
        $('<button type="button" class="btn btn-info plusminus-plus"><span class="glyphicon glyphicon-plus"></span></button>').on("click", function() {
            self.value = humanize(parseFloat(self.value) + options.step,options.precision);
            if (parseFloat(self.value) > parseFloat(options.max)){
                self.value = options.max;
            }
            $('.plusminus-span-value').empty().append(self.value);
        }).appendTo(this.btnGroup);
        
        popover.addClass(options.placement);
        popover.addClass('plusminus-align-' + options.align);
        input.on('focus.plusminus click.plusminus', $.proxy(this.show, this))

	}
    
    function humanize(x,precision) {
        return x.toFixed(precision).replace(/\.?0*$/, '');
    }
                                                    
    function raiseCallback(callbackFunction) {
		if (callbackFunction && typeof callbackFunction === "function") {
			callbackFunction();
		}
	}
    
    // Default options
	PlusMinus.DEFAULTS = {
		'default': 20.0,       // default time, 'now' or '13:14' e.g.
		placement: 'bottom', // clock popover placement
		align: 'top',       // popover arrow align
		step: 0.5,
		precision: 1,
		min: 15,
		max: 30
	};
    
    // Show or hide popover
	PlusMinus.prototype.toggle = function(){
		this[this.isShown ? 'hide' : 'show']();
	};
    
    // Set popover position
	PlusMinus.prototype.locate = function(){
		var element = this.element,
			popover = this.popover,
			offset = element.offset(),
			width = element.outerWidth(),
			height = element.outerHeight(),
			placement = this.options.placement,
			align = this.options.align,
			styles = {},
			self = this;

		popover.show();

		// Place the popover
		switch (placement) {
			case 'bottom':
				styles.top = offset.top + height;
				break;
			case 'right':
				styles.left = offset.left + width;
				break;
			case 'top':
				styles.top = offset.top - popover.outerHeight();
				break;
			case 'left':
				styles.left = offset.left - popover.outerWidth();
				break;
		}

		// Align the popover arrow
		switch (align) {
			case 'left':
				styles.left = offset.left;
				break;
			case 'right':
				styles.left = offset.left + width - popover.outerWidth();
				break;
			case 'top':
				styles.top = offset.top;
				break;
			case 'bottom':
				styles.top = offset.top + height - popover.outerHeight();
				break;
		}

		popover.css(styles);
	};
    
    // Show popover
	PlusMinus.prototype.show = function(e){
		// Not show again
		if (this.isShown) {
			return;
		}

		raiseCallback(this.options.beforeShow);
		var self = this;

		// Initialize
		if (! this.isAppended) {
			// Append popover to body
			$body = $(document.body).append(this.popover);

			// Reset position when resize
			$win.on('resize.plusminus' + this.id, function(){
				if (self.isShown) {
					self.locate();
				}
			});

			this.isAppended = true;
		}

		// Get the time
		this.value = (this.input.prop('value') || this.options['default']);
        this.spanValue.html(this.value);

		// Set position
		this.locate();
        
		this.isShown = true;

		// Hide when clicking or tabbing on any element except the clock, input and addon
		$doc.on('click.plusminus.' + this.id + ' focusin.plusminus.' + this.id, function(e){
			var target = $(e.target);
			if (target.closest(self.popover).length === 0 &&
					target.closest(self.input).length === 0) {
				self.done();
			}
		});

		// Hide when ESC is pressed
		$doc.on('keyup.plusminus.' + this.id, function(e){
			if (e.keyCode === 27) {
				self.hide();
			}
		});

		raiseCallback(this.options.afterShow);
	};
    
    // Hide popover
	PlusMinus.prototype.hide = function(){
		raiseCallback(this.options.beforeHide);

		this.isShown = false;

		// Unbinding events on document
		$doc.off('click.plusminus.' + this.id + ' focusin.plusminus.' + this.id);
		$doc.off('keyup.plusminus.' + this.id);

        //this.input.prop('value', this.value);
		this.popover.hide();

		raiseCallback(this.options.afterHide);
	};
    
    // Hours and minutes are selected
	PlusMinus.prototype.done = function() {
		raiseCallback(this.options.beforeDone);
        console.log("OUT");
		this.hide();
		var last = this.input.prop('value'),
			value = this.value;

		this.input.prop('value', value);
		if (value !== last) {
			this.input.triggerHandler('change');
			if (! this.isInput) {
				this.element.trigger('change');
			}
		}
        
		this.input.trigger('blur');

		raiseCallback(this.options.afterDone);
	};

	// Remove clockpicker from input
	PlusMinus.prototype.remove = function() {
		this.element.removeData('plusminus');
		this.input.off('focus.plusminus click.plusminus');
		if (this.isShown) {
			this.hide();
		}
		if (this.isAppended) {
			$win.off('resize.plusminus' + this.id);
			this.popover.remove();
		}
	};
    
    // Extends $.fn.clockpicker
	$.fn.plusminus = function(option){
		var args = Array.prototype.slice.call(arguments, 1);
		return this.each(function(){
			var $this = $(this),
				data = $this.data('plusminus');
			if (! data) {
				var options = $.extend({}, PlusMinus.DEFAULTS, $this.data(), typeof option == 'object' && option);
				$this.data('plusminus', new PlusMinus($this, options));
			} else {
				// Manual operatsions. show, hide, remove, e.g.
				if (typeof data[option] === 'function') {
					data[option].apply(data, args);
				}
			}
		});
	};
}());
